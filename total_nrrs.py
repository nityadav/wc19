from collections import defaultdict

with open('all_run_rates.tsv') as inp_f:
    all_rrs = []
    nrrs = defaultdict(lambda: 0.0)
    total_m = defaultdict(lambda: 0)
    for line in inp_f:
        parts = line.strip().split('\t')
        rr = float(parts[2])
        nrrs[parts[0]] += rr
        total_m[parts[0]] += 1
        nrrs[parts[1]] -= rr
        total_m[parts[1]] += 1

for k in nrrs:
    print(k + ": " + str(nrrs[k]/total_m[k]))
