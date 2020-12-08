import sys
import os
import numpy as np

from fairseq.bert_score.score import score

def main(bert_model, preds_path, refs_path, output_path, device):

    # Predictions
    preds_file = open(preds_path)
    preds_list = []
    for line in preds_file:
        line = line.strip().replace('\n','')
        preds_list.append(line)
    preds_file.close()
    # References
    refs_file = open(refs_path)
    refs_list = []
    for line in refs_file:
        line = line.strip().replace('\n', '')
        refs_list.append(line)
    refs_file.close()

    # Scorer
    results = score(preds_list, refs_list, model_type=bert_model, device=device, verbose=True)
    output_file = open(output_path, 'w')
    avg_results = []
    for res in results:
        val = np.average(res.numpy())
        avg_results.append(val)
    output_file.write('Prec: ' + str(avg_results[0]) + ' Rec: ' + str(avg_results[1]) + ' F1: ' +str(avg_results[2]))
    output_file.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
