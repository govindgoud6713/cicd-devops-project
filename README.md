# My First CI/CD DevOps Project

A small Flask web application that we will use to learn the DevOps workflow.

## Project roadmap

1. Run the application locally.
2. Run automated tests.
3. Build and run a Docker image locally.
4. Create a Docker Hub repository and push the image.
5. Push the source code to GitHub.
6. Use GitHub Actions to test, build, and publish the Docker image.
7. Deploy the app to local Kubernetes (kind or Minikube).
8. Learn Kubernetes deployments, services, scaling, and updates.
9. Optional cloud stage: provision infrastructure with Terraform on AWS and deploy to it.

## Local run

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 and http://127.0.0.1:5000/health.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Docker

```bash
docker build -t devops-demo:1.0 .
docker run --name devops-demo -p 5000:5000 devops-demo:1.0
```

Open http://localhost:5000. Stop the container with Ctrl+C, then remove it with:

```bash
docker rm devops-demo
```

## GitHub Actions / Docker Hub

The workflow in `.github/workflows/docker-publish.yml` runs tests and publishes an image when code is pushed to `main`.

Configure these GitHub repository Actions secrets before enabling the publish step:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Replace `YOUR_DOCKERHUB_USERNAME` in the workflow with your Docker Hub username.

Never commit passwords, access tokens, cloud keys, or kubeconfig files.

## Kubernetes

The `k8s/` directory contains a Deployment and Service. Before applying them, replace
`YOUR_DOCKERHUB_USERNAME` in `k8s/deployment.yaml` with your Docker Hub username and
make sure the image tag exists in Docker Hub.

```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get services
```

For local clusters, use the NodePort service and your cluster's documented access method.

## Terraform / cloud

We will add and apply Terraform only after the local app, Docker, GitHub Actions, and
local Kubernetes stages work. Cloud infrastructure can create charges. We will review
the plan, region, resources, and cleanup commands before creating anything.
