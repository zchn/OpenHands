# OpenHands Kubernetes Deployment

This directory contains Kubernetes configurations for deploying OpenHands in a Kubernetes cluster.

## Components

- `namespace.yaml`: Creates a dedicated namespace for OpenHands
- `configmap.yaml`: Contains configuration for OpenHands application
- `deployment.yaml`: Deploys the OpenHands application container
- `pvc.yaml`: Persistent Volume Claim for OpenHands state
- `service.yaml`: Service and Ingress configurations for accessing OpenHands

## Prerequisites

1. A Kubernetes cluster
2. kubectl configured to access your cluster
3. Storage class available in your cluster
4. Ingress controller installed (if using the provided Ingress configuration)

## Deployment Steps

1. Create the namespace:
```bash
kubectl apply -f namespace.yaml
```

2. Create the ConfigMap:
```bash
kubectl apply -f configmap.yaml
```

3. Create the PVC:
```bash
kubectl apply -f pvc.yaml
```

4. Deploy the application:
```bash
kubectl apply -f deployment.yaml
```

5. Create the Service and Ingress:
```bash
kubectl apply -f service.yaml
```

Or apply all at once:
```bash
kubectl apply -f .
```

## Configuration

1. Update `configmap.yaml` with your desired configuration values
2. Modify storage class in `pvc.yaml` according to your cluster's available options
3. Adjust the Ingress configuration in `service.yaml` based on your cluster's setup

## Important Notes

- The deployment requires access to the Docker socket (`/var/run/docker.sock`) for running sandboxed environments
- The container runs in privileged mode to access Docker
- Persistent storage is used to maintain OpenHands state
- Default storage request is 1Gi, adjust as needed

## Security Considerations

- The deployment runs in privileged mode and has access to the Docker socket. Ensure proper security measures are in place.
- Consider implementing network policies to restrict pod communication
- Review and adjust RBAC permissions as needed for your environment