# Template for deploying [Gradio Apps](https://gradio.app/demos/)

## SECRET values to be provided by Tapu on request:

- `<SERVICE_ACCOUNT_EMAIL>`: Service Account Email with necessary permissions for deployment.

## Prerequisite libraries/softwares

- Required for Deployment:
  - [google-cloud-sdk](https://cloud.google.com/sdk/docs/install)
  - Docker Desktop
- Required for local testing:
  - libraries in `requirements.txt`

## Command for local testing:

Start the Local Gradio Server at `http://0.0.0.0:8080` using command:

```
python app.py
```

## Authorize Docker to push images to Google Cloud Registry

After installing both `google-cloud-sdk` & `docker`:

1. [Authorize Google Cloud SDK](https://cloud.google.com/sdk/docs/authorizing) using your obv.ai User email.

## App structure Requirements:

- `app.py` is the main python executable.
- Always keep `app.py` in top directory, including any files imported by `app.py`.
- If your gradio app requires libraries other than the ones included in `requirements.txt`, add them to `requirements.txt`.

## Terminal Command for listing deployed Services:

```
gcloud run services list --region us-central1 --impersonate-service-account=<SERVICE_ACCOUNT_EMAIL>
```

## Terminal Command for deleting deployed Notebook API Service:

```
gcloud run services delete <UNIQUE_PROJECT_NAME> --region us-central1 --impersonate-service-account=<SERVICE_ACCOUNT_EMAIL>
```

## Instructions for deployment:

Use `build_run.sh` to deploy Gradio App as a microservice to **Google Cloud Run**.
This script requires 2 argument values:

- `--name`: A unique name for this Jupyter Notebook API Service. Otherwise, this will **OVERRIDE** existing Service with the same name. Use terminal command above to confirm your Service name is unique.
- `--svc-acc-email`: Service Account Email `<SERVICE_ACCOUNT_EMAIL>`. Will be provided by Tapu on request

```
# If running for first time:
chmod +x build_run.sh
# Start deployment
./build_run.sh --name <UNIQUE_PROJECT_NAME> --svc-acc-email <SERVICE_ACCOUNT_EMAIL>
```

After successful execution, deployed Gradio App will be accessible via the **Service URL**. This URL is included in the Cloud Build logs; below is an example snippet of the output:

```
latest: digest: sha256:50a2e4693dbea7b37a4dd65ca2d9045e9b889cf3d4948118562e861617cc407f size: 4069
Deploying container to Cloud Run service [gradio-app] in project [xx-xxx-xxxx] region [us-central1]
✓ Deploying new service... Done.
  ✓ Creating Revision... Creating Service.
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [gradio-app] revision [gradio-app-00001-toj] has been deployed and is serving 100 percent of traffic.
Service URL: https://gradio-app-xl3243gfga-uc.a.run.app
```
