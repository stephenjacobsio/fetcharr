# FetchArr

![Python](https://img.shields.io/badge/Python-3.13+-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blueviolet)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-yellow)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-lightorange)](https://www.buymeacoffee.com/rootiovo)

**FetchArr** is a powerful metadata aggregation and enrichment tool for your media library. It integrates with **Jellyfin**, **Radarr**, **Sonarr**, and external APIs like **TMDb**, **IMDb**, and **TVDb** to fetch, enrich, and store metadata for movies and TV shows.

---

## Features

| Feature                 | Status        | Description                                       |
|-------------------------|---------------|---------------------------------------------------|
| **Integrations**        | ✅ Implemented | Fetch metadata from Jellyfin, Radarr, and Sonarr. |
| **Metadata Enrichment** | ✅ Implemented | Enhance data using TMDb, IMDb, and TVDb.          |
| **Efficient Caching**   | ✅ Implemented | Redis-backed caching for fast responses.          |
| **Persistent Storage**  | ✅ Implemented | PostgreSQL-based long-term metadata storage.      |
| **REST API**            | ✅ Implemented | Simple API for querying and managing metadata.    |

---

## Getting Started

### Prerequisites
- Python 3.13+
- Docker and Docker Compose
- API keys for TMDb, IMDb, TVDb, Jellyfin, Radarr, and Sonarr

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/fetcharr.git
   cd fetcharr
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add:
   ```ini
   DATABASE_URL=postgresql://user:password@db/media_aggregator
   REDIS_URL=redis://redis:6379
   TMDB_API_KEY=your_tmdb_api_key
   IMDB_API_KEY=your_imdb_api_key
   TVDB_API_KEY=your_tvdb_api_key
   JELLYFIN_API_KEY=your_jellyfin_api_key
   RADARR_API_KEY=your_radarr_api_key
   SONARR_API_KEY=your_sonarr_api_key
   TZ=your_timezone
   UID=your_user_id
   GID=your_group_id
   ```

3. **Build and Start the Application**:
   ```bash
   docker-compose up --build -d
   ```

4. **Access the API**:
   - Visit `http://localhost:8000/docs` for the interactive API documentation.
   - Access `http://localhost:8000` to use FetchArr.

---

## API Endpoints

### Metadata Management
- `GET /metadata` - List all stored metadata.
- `POST /metadata/enrich/{title}` - Enrich metadata for a specific title.

### Jellyfin Integration
- `GET /jellyfin/library` - Fetch the media library from Jellyfin.

### Radarr Integration
- `GET /radarr/movies` - Retrieve movie metadata from Radarr.

### Sonarr Integration
- `GET /sonarr/series` - Retrieve TV show metadata from Sonarr.

---

## Roadmap

| Feature                    | Status    | Description                                |
|----------------------------|-----------|--------------------------------------------|
| **Plex Integration**       | ⏳ Planned | Add metadata support for Plex.             |
| **Emby Integration**       | ⏳ Planned | Add metadata support for Emby.             |
| **Advanced Filtering**     | ⏳ Planned | Filter by genre, rating, and release year. |
| **Frontend UI**            | ⏳ Planned | Web dashboard for metadata visualization.  |
| **Enhanced Notifications** | ⏳ Planned | Custom notifications for new content.      |

---

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
## Support

If you like this project, consider buying me a coffee to support further development:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-lightorange)](https://www.buymeacoffee.com/rootiovo)

---

<p align="center">Made with ❤️ by <a href="https://stephenjacobs.io">Stephen Jacobs</a></p>
