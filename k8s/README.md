# OpenHands Kubernetes Configurations

This directory contains Kubernetes configurations for deploying OpenHands in a Kubernetes cluster.

## Components

1. **Backend Deployment & Service** (`backend-deployment.yaml`)
   - Deploys the OpenHands backend server
   - Exposes port 3000
   - Uses ClusterIP service type
   - Resource limits:
     - Memory: 512Mi-1Gi
     - CPU: 250m-500m

2. **Frontend Deployment & Service** (`frontend-deployment.yaml`)
   - Deploys the OpenHands frontend server
   - Exposes port 3001
   - Uses ClusterIP service type
   - Resource limits:
     - Memory: 256Mi-512Mi
     - CPU: 100m-200m

3. **Ingress Configuration** (`ingress.yaml`)
   - Exposes both frontend and backend services
   - Configures CORS and path routing
   - Routes:
     - `/api/*` -> backend service
     - `/*` -> frontend service
   - Hosts:
     - work-1-abdcoxuzwicybucg.prod-runtime.all-hands.dev
     - work-2-abdcoxuzwicybucg.prod-runtime.all-hands.dev

## Prerequisites

Before deploying:
1. Build the Docker images for both frontend and backend:
   ```bash
   # From repository root
   docker build -t openhands-backend -f containers/backend/Dockerfile .
   docker build -t openhands-frontend -f containers/frontend/Dockerfile .
   ```

2. Ensure your Kubernetes cluster has:
   - NGINX Ingress Controller installed
   - Sufficient resources for the deployments

## Deployment

Apply the configurations in the following order:

```bash
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f ingress.yaml
```

## Verification

Check the deployment status:
```bash
kubectl get pods -l app=openhands
kubectl get services -l app=openhands
kubectl get ingress openhands-ingress
```

## Configuration

The services are configured through environment variables:

### Backend
- `HOST`: Set to "0.0.0.0" to allow external connections
- `PORT`: Set to 3000

### Frontend
- `VITE_BACKEND_HOST`: Points to the backend service
- `VITE_FRONTEND_PORT`: Set to 3001
- `HOST`: Set to "0.0.0.0" to allow external connections