import robust
import argparse

def robust_bias_aware():
    parser = argparse.ArgumentParser(description='Description of your program')
    
    # add arguments
    parser.add_argument('--seeds', type=str, help='Path to seeds file', required=True)
    parser.add_argument('--outfile', type=str, help='Output file name', required=True)
    parser.add_argument('--network', type=str, default='BioGRID', help='Network type')
    parser.add_argument('--namespace', type=str, default='GENE_SYMBOL', help='Namespace')
    parser.add_argument('--alpha', type=float, default=0.25, help='Alpha value')
    parser.add_argument('--beta', type=float, default=0.9, help='Beta value')
    parser.add_argument('--n', type=int, default=30, help='n value')
    parser.add_argument('--tau', type=float, default=0.1, help='Tau value')
    parser.add_argument('--study_bias_scores', type=str, default='BAIT_USAGE', help='Study bias scores')
    parser.add_argument('--gamma', type=float, default=1.0, help='Gamma value')
    
    args = parser.parse_args()

    seeds = args.seeds
    outfile = args.outfile
    network = args.network
    namespace = args.namespace
    alpha = args.alpha
    beta = args.beta
    n = args.n
    tau = args.tau
    study_bias_scores = args.study_bias_scores
    gamma = args.gamma

    if not seeds:
        raise ValueError("Missing required parameter: 'seeds'")
    if not outfile:
        raise ValueError("Missing required parameter: 'outfile'")
    
    _ , _ = robust.run(seeds, network, namespace, alpha, beta, n, tau, study_bias_scores, gamma, outfile)


if __name__ == "__main__":
    robust_bias_aware()