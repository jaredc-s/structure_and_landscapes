"""
This module contains a class (Run) that encapsulate the
parameters and results of a single evolutionary simulation.
"""
import persistence

from ..organism.bitstring import organism as bitstring_organism
from ..organism.bitstring.bitstring import Bitstring
from ..population.population import Population
from ..population.meta_population import MetaPopulation, StructuredPopulation
from ..organism.bitstring.nk_model import nk_model as nk_model
from ..organism.bitstring import bitstring
from ..organism.bitstring.nk_model import organism as nk_organism
from ..organism.rna import organism as rna_organism


class Run(object):
    """
    Object holding the save data.
    """
    def __init__(
            self,
            initial_population,
            final_population,
            parameters,
            shelf_filepath,
            other_data=None):
        self.initial_population = initial_population
        self.final_population = final_population
        self.parameters = parameters
        self.shelf_filepath = shelf_filepath
        self.other_data = other_data
        persistence.save_with_unique_key(self.shelf_filepath, self)


def run_population(population, number_of_generations):
    for gen in range(number_of_generations):
        print("Gen: {}".format(gen))
        population.advance_generation()
    return population


class OrgException(Exception):
    pass


def process_initial_org(parameter_settings):
    if parameter_settings["Organism Type"] == "RNA":
        org = rna_organism.random_organism()
    elif parameter_settings["Organism Type"] == "Bitstring":
        org = bitstring_organism.random_organism(
            int(parameter_settings["Length of Org"]))
    elif parameter_settings["Organism Type"] == "NK Model":
        length = int(parameter_settings["Length of Org"])
        b = bitstring.random_string(length)
        nk_fac = nk_model.NKModelFactory()
        if "Number of Genes" not in parameter_settings:
            number_of_genes = 1
        else:
            number_of_genes = int(parameter_settings["Number of Genes"])
        k_total = int(parameter_settings["K-total"])
        if number_of_genes == 1:
            unique_nk_model = nk_fac.non_consecutive_dependencies(
                n=length, k=k_total)
        else:
            length_of_gene = int(parameter_settings["Length of Gene"])
            k_intra = int(parameter_settings["K-intra"])

            unique_nk_model = nk_fac.non_consecutive_dependencies_multigene(
                n_per_gene=length_of_gene,
                number_of_genes=number_of_genes,
                k_intra_gene=k_intra,
                k_total=k_total)
        org = nk_organism.Organism(value=b, nk_model=unique_nk_model)
    else:
        raise OrgException("Not a valid org type")
    return org


def process_initial_population(parameter_settings):
    org = process_initial_org(parameter_settings)
    orgs_per_population = int(parameter_settings["Orgs per Population"])
    org_list = [org for _ in range(orgs_per_population)]
    mutation_rate = float(parameter_settings["Mutation Rate"])

    if ("Number of Subpopulations in Width" in parameter_settings and
            "Number of Subpopulations in Height" in parameter_settings):
        width = int(parameter_settings["Number of Subpopulations in Width"])
        height = int(parameter_settings["Number of Subpopulations in Height"])
        assert(width > 0)
        assert(height > 0)
        number_of_pops = width * height
    elif "Number of Populations" in parameter_settings:
        number_of_pops = int(parameter_settings["Number of Populations"])
    else:
        number_of_pops = 1
    if number_of_pops <= 1:
        return Population(org_list, mutation_rate=mutation_rate)

    mig_rate = float(parameter_settings["Migration Rate"])
    prop_miged = float(parameter_settings[
        "Proportion of Population Migrated"])

    pop_list = [Population(org_list, mutation_rate=mutation_rate)
                for _ in range(number_of_pops)]
    if "Migration Type" in parameter_settings:
        assert(parameter_settings["Migration Type"] in
               {"Local", "Global", "Restricted", "Unrestricted"})
        if parameter_settings["Migration Type"] in {"Local", "Restricted"}:
            return StructuredPopulation(
                pop_list,
                migration_rate=mig_rate,
                proportion_of_pop_migrated=prop_miged,
                width=width,
                height=height)
    return MetaPopulation(
        pop_list,
        migration_rate=mig_rate,
        proportion_of_pop_migrated=prop_miged)


def process_and_run(parameter_settings):
    initial_population = process_initial_population(parameter_settings)
    number_of_generations = int(
        parameter_settings["Number of Generations"])
    final_population = run_population(
        initial_population,
        number_of_generations)
    shelf_filepath = parameter_settings["Output File Path"]
    Run(
        initial_population=initial_population,
        final_population=final_population,
        parameters=parameter_settings,
        shelf_filepath=shelf_filepath)
