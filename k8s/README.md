# OpenHands Kubernetes Deployment

This directory contains Kubernetes configurations for deploying OpenHands in a production environment.

## Overview

OpenHands uses a single Docker image `ghcr.io/all-hands-ai/openhands:main` that contains both the frontend and backend code. The image is built and published automatically via GitHub Actions when changes are merged to the main branch.

## Deployment Configuration

The deployment is configured to work with two runtime environments:

1. **work-1** environment:
   - Host: work-1-abdcoxuzwicybucg.prod-runtime.all-hands.dev
   - Port: 12000

2. **work-2** environment:
   - Host: work-2-abdcoxuzwicybucg.prod-runtime.all-hands.dev
   - Port: 12001

## Components

### Frontend Service
- React/Vite application serving the web UI
- Runs on ports 12000/12001 (work-1/work-2)
- Environment variables configured for backend communication
- CORS and iframe access enabled
- Resource limits:
  - Memory: 512Mi (limit), 256Mi (request)
  - CPU: 200m (limit), 100m (request)

### Backend Service
- FastAPI server providing API endpoints
- Runs on ports 12000/12001 (work-1/work-2)
- Handles API requests at /api endpoint
- CORS enabled for frontend access
- Resource limits:
  - Memory: 1Gi (limit), 512Mi (request)
  - CPU: 500m (limit), 250m (request)

### Ingress Configuration
- Routes /api/* to the backend service
- Routes /* to the frontend service
- Enables CORS headers
- Supports both work-1 and work-2 environments

## Deployment Instructions

1. Apply the Kubernetes configurations:
```bash
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f ingress.yaml
```

2. Verify the deployment:
```bash
# Check pod status
kubectl get pods -l app=openhands

# Check services
kubectl get services -l app=openhands

# Check ingress rules
kubectl get ingress openhands-ingress

# View pod logs
kubectl logs -l app=openhands -l component=frontend
kubectl logs -l app=openhands -l component=backend
```

3. Access the application:
- Frontend: https://work-1-abdcoxuzwicybucg.prod-runtime.all-hands.dev or https://work-2-abdcoxuzwicybucg.prod-runtime.all-hands.dev
- Backend API: https://work-1-abdcoxuzwicybucg.prod-runtime.all-hands.dev/api or https://work-2-abdcoxuzwicybucg.prod-runtime.all-hands.dev/api