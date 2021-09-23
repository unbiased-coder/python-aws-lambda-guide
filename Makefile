upload:
	echo "Preparing zip file for upload..."
	zip unbiased-coder-lambda.zip test_lambda.py
	echo "Updating Lambda code"
	aws lambda update-function-code --function-name unbiased_coder_lambda --zip-file fileb://unbiased-coder-lambda.zip
	aws lambda update-function-configuration --function-name unbiased_coder_lambda --handler test_lambda.lambda_handler
run:
	python ./invoke_lambda.py
	