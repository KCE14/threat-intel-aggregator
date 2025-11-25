# Threat Intel Aggregator

A CLI tool for querying threat intelligence APIs.

## Setup

### Local Development
1. Create `config/config.yaml`
2. Add your API keys
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python src/main.py <IP_ADDRESS>`
5. Use `--save` flag for YAML file output

### Docker
1. Build the image:
   ```bash
   docker build -t threat-intel-aggregator:latest .
   ```

2. Run with an IP address:
   ```bash
   docker run --rm -v /$(pwd)/config:/app/config threat-intel-aggregator:latest 8.8.8.8
   ```

3. Save output to file:
   ```bash
   docker run --rm -v /$(pwd)/config:/app/config threat-intel-aggregator:latest 8.8.8.8 --save
   ```

**Note:** The `-v` flag mounts your local `config/` directory so the container can access your API keys.

## Progress

### Phase 1: AbuseIPDB Integration
- [x] Project structure
- [x] API client
- [x] CLI interface
- [x] YAML output

### Phase 2: Docker Integration
- [x] Build container image
- [x] Test container locally
- [x] Volume mounting for config