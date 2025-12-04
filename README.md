# AstronRPA (English Version)

## Quick Start - Backend

### Prerequisites
- Docker & Docker Compose

### Start Backend Services

```bash
cd docker
cp .env.example .env
docker compose up -d
```

### Services

| Service | URL |
|---------|-----|
| Robot Service | http://localhost:8040 |
| Resource Service | http://localhost:8030 |
| OpenAPI Service | http://localhost:8020 |
| AI Service | http://localhost:8010 |
| MinIO Console | http://localhost:9001 |

### Commands

```bash
# Stop
docker compose stop

# View logs
docker compose logs -f [service-name]

# Restart
docker compose restart [service-name]
```

### Frontend - Prebuilt App

Download: [AstronRPA Desktop App](https://drive.google.com/file/d/1H6Di2uwDwnP6ht2vRDNEXR6dU5NIiiiN/view?usp=sharing)
