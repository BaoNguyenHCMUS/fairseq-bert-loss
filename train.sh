DATASET_FOLDER=datasets/de-en_TEDtalks
MODEL=models/BAS_TRANS
CUDA_VISIBLE_DEVICES=-1 fairseq-train $DATASET_FOLDER/$MODEL/preprocessed_data \
             --lr 0.0002 -s de -t en --optimizer adam --max-tokens 1024 --dropout 0.1 \
             --arch transformer_iwslt_de_en --save-dir $DATASET_FOLDER/$MODEL/checkpoints \
             --no-epoch-checkpoints --max-epoch 50  --lr-scheduler inverse_sqrt \
             --warmup-updates 4000 --warmup-init-lr '1e-07' --min-lr '1e-09' \
             --adam-betas '(0.9, 0.98)' --weight-decay 0.0001 \
             --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
             --no-epoch-checkpoints