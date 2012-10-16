import main

fp = open("parameters.cfg")
fp.readline()
fp.readline()
fp.readline()
rate = fp.readline().split(":")[1]
num_org = fp.readline().split(":")[1]
pops = fp.readline().split(":")[1]
mig_rate = fp.readline().split(":")[1]
swap_rate = fp.readline().split(":")[1]
org_type = fp.readline().split(":")[1]
len_gene = fp.readline().split(":")[1]
num_gene = fp.readline().split(":")[1]
updates = fp.readline().split(":")[1]

if org_type == "RNA":
    if pops > 1:
        org = rna_organism.random_organism()
        org_list = [org for _ in range(num_org)]
        pop_list = [Population(org_list) for _ in range(pops)]
        structured_pop = Structured_Population(pop_list,
                                           migration_rate=mig_rate,
                                           proportion_of_pop_swapped=sap_rate)
        run_struc(structured_pop)

    else:
        org = rna_organism.random_organism()
        org_list = [org for _ in range(num_org)]
        pop_list = [Population(org_list) for _ in range(pops)]
        structured_pop = Structured_Population(pop_list,
                                           migration_rate=0,
                                           proportion_of_pop_swapped=0)
        run_struc(structured_pop)        

elif org_type == "Bitstring":
    pass
elif org_type == "NK Model":
    
else:
    raise TypeError("Not a valid org type")
