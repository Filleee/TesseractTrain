rm -rf data/finetuned_model/*
OMP_THREAD_LIMIT=8 lstmtraining \
	--continue_from data/model/ind.lstm \
	--model_output data/finetuned_model/ \
	--traineddata data/tess_data/ind.traineddata \
	--train_listfile data/output/ind.training_files.txt \
	--max_iterations 400
