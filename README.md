# FetchArr

![Python](https://img.shields.io/badge/Python-3.13+-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blueviolet)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-yellow)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-lightorange)](https://www.buymeacoffee.com/rootiovo)

**FetchArr** is a metadata aggregation and enrichment tool for your media library. It integrates with **Jellyfin**, **Radarr**, **Sonarr**, and external APIs like **TMDb**, **IMDb**, and **TVDb** to fetch, enrich, and provide comprehensive metadata for movies and TV shows.

---

## Features

| Feature                 | Status                                                                      | Description                                                |
|-------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------|
| **Integrations**        | ![Implemented](https://img.shields.io/badge/Status-Implemented-brightgreen) | Fetch metadata directly from Jellyfin, Radarr, and Sonarr. |
| **Metadata Enrichment** | ![Implemented](https://img.shields.io/badge/Status-Implemented-brightgreen) | Enhance data with information from TMDb, IMDb, and TVDb.   |
| **Efficient Caching**   | ![Implemented](https://img.shields.io/badge/Status-Implemented-brightgreen) | Redis-backed caching for faster responses.                 |
| **Persistent Storage**  | ![Implemented](https://img.shields.io/badge/Status-Implemented-brightgreen) | PostgreSQL for long-term metadata storage.                 |
| **REST API**            | ![Implemented](https://img.shields.io/badge/Status-Implemented-brightgreen) | Easy-to-use API for querying and managing metadata.        |

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
   ```env
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
   docker-compose up --build
   ```

4. **Access the API**:
   Visit `http://localhost:8000` to interact with FetchArr's REST API.

---

## API Endpoints

### Metadata Management
- `GET /metadata` - List all metadata stored in the database.
- `POST /enrich/{title}` - Enrich metadata for a specific title.

### Jellyfin Integration
- `GET /jellyfin/library` - Fetch media library from Jellyfin.

### Radarr Integration
- `GET /radarr/movies` - Fetch movie library from Radarr.

### Sonarr Integration
- `GET /sonarr/series` - Fetch TV series library from Sonarr.

---

## Roadmap

| Feature                    | Status                                                         | Description                                       |
|----------------------------|----------------------------------------------------------------|---------------------------------------------------|
| **Plex Integration**       | ![Planned](https://img.shields.io/badge/Status-Planned-yellow) | Add support for fetching metadata from Plex.      |
| **Emby Integration**       | ![Planned](https://img.shields.io/badge/Status-Planned-yellow) | Add support for fetching metadata from Emby.      |
| **Advanced Filtering**     | ![Planned](https://img.shields.io/badge/Status-Planned-yellow) | Enable filtering by genre, rating, release year.  |
| **Frontend UI**            | ![Planned](https://img.shields.io/badge/Status-Planned-yellow) | Build a web dashboard for metadata visualization. |
| **Enhanced Notifications** | ![Planned](https://img.shields.io/badge/Status-Planned-yellow) | Add support for custom notifications.             |

---

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
## Support

If you like this project, consider buying me a coffee to support further development:



---
<div style="text-align: center">
  <p>Made with ❤️ by <a href="https://stephenjacobs.io">Stephen Jacobs</a></p>
</div>

