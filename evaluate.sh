lstmeval --model data/tess_data/_checkpoint \
  --traineddata data/tess_data/ind.traineddata \
  --eval_listfile data/output/ind.training_files.txt \
  --verbosity 2


#--model_dat takes the extracted model as input
#--traineddata takes the data it was trained on
#--eval_listfile takes the files that are to be evaluated