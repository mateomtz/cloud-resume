.PHONY: build

build:
	sam build  --profile Sam_Deploy_Updated-676206935526

deploy-infra:
	sam build --profile Sam_Deploy_Updated-676206935526 & sam deploy --profile Sam_Deploy_Updated-676206935526

deploy-site:
	aws s3 sync ./resume-site s3://my-resume-website-mm --profile Sam_Deploy_Updated-676206935526
