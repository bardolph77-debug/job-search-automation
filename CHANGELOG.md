# Changelog

All notable changes to the Job Search Automation project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive job board scraper architecture
- Base scraper abstract class for extensible scraping
- Dynamic scraper registry system for managing multiple scrapers
- Duunitori scraper implementation for Finnish job board
- Configuration system with YAML support for job board settings
- Requirements file with all necessary dependencies

### Changed
- Updated config.yaml with comprehensive job scraper settings
- Updated requirements.txt with web scraping and automation dependencies

## [0.2.0] - 2025-11-09

### Added
- **Scraper Infrastructure** (Nov 9, 2025)
  - Created `base_scraper.py`: Abstract base class defining scraper interface
    - Rate limiting support
    - Standardized job data structure
    - Abstract methods for URL building and data extraction
  - Created `scraper_registry.py`: Dynamic scraper management system
    - Automatic scraper discovery and registration
    - Factory pattern for scraper instantiation
    - Retrieval of available scrapers
  - Created `duunitori_scraper.py`: First concrete scraper implementation
    - Scrapes Duunitori.fi (Finland's largest job board)
    - Search by keywords and location
    - Extracts job title, company, location, salary, description, and URL
    - Implements proper rate limiting and error handling

- **Configuration Updates** (Nov 9, 2025)
  - Updated `config.yaml` with job scraper settings
    - Configured 5 job boards: Duunitori, Työmarkkinatori, Jobly, Oikotie, Monster
    - Added rate limiting settings (1.0 second default)
    - Configured search parameters (keywords, locations, max results)
    - Added job filtering criteria (min salary, required skills, experience levels)
    - Configured storage settings (database type, output format)

  - Updated `requirements.txt` with scraping dependencies
    - beautifulsoup4==4.12.2: HTML parsing
    - requests==2.31.0: HTTP requests
    - lxml==4.9.3: XML/HTML processing
    - selenium==4.15.0: Browser automation
    - pandas==2.1.3: Data manipulation
    - pyyaml==6.0.1: YAML configuration
    - python-dotenv==1.0.0: Environment variables
    - schedule==1.2.0: Task scheduling
    - sqlalchemy==2.0.23: Database ORM
    - psycopg2-binary==2.9.9: PostgreSQL adapter
    - notion-client==2.2.1: Notion API integration

## [0.1.0] - 2025-10-27

### Added
- **Project Initialization**
  - Initial repository setup
  - Created comprehensive README.md with project architecture
  - Defined system modules and components
  - Established checkpoint-based development approach

- **Directory Structure**
  - `automation_scripts/`: Automation workflow scripts
  - `docs/`: Project documentation including architecture.md
  - `n8n_flows/`: n8n workflow definitions
  - `notion_sync/`: Notion database synchronization
  - `scrapers/`: Web scraping modules
  - `src/`: Core source code including orchestrator.py
  - `templates/`: Jinja templates for document generation
  - `tests/`: Test files and fixtures

- **Documentation**
  - Architecture overview with module descriptions
  - Core objectives and system design
  - Development checkpoints and phases
  - Actionable build steps with code examples
  - Technology stack documentation

### Infrastructure
- Set up folder structure with README files
- Created .gitkeep files for empty directories
- Established coding guidelines and standards

---

## Release Notes

### Version 0.2.0 - Scraper Foundation
**Release Date:** November 9, 2025

This release establishes the core scraper infrastructure for the job search automation system. The architecture is now in place to support multiple job boards through a flexible, extensible framework.

**Key Features:**
- Modular scraper architecture with base class pattern
- Dynamic scraper registration and discovery
- First working scraper for Duunitori.fi
- Comprehensive configuration system
- Production-ready dependencies

**Next Steps:**
- Implement additional job board scrapers (Työmarkkinatori, Jobly)
- Create job orchestrator for managing multiple scrapers
- Develop main entry point script
- Add database integration for job storage
- Implement testing suite

### Version 0.1.0 - Project Foundation
**Release Date:** October 27, 2025

Initial project setup with documentation, directory structure, and architectural planning.

---

## Upcoming Features

### Planned for v0.3.0
- [ ] Työmarkkinatori scraper implementation
- [ ] Jobly scraper implementation
- [ ] Job orchestrator for coordinating multiple scrapers
- [ ] Main script with CLI interface
- [ ] Database integration for job storage
- [ ] Job deduplication logic
- [ ] Data normalization across different sources

### Planned for v0.4.0
- [ ] Job matching system with user profiles
- [ ] Resume parsing and skill extraction
- [ ] Job filtering and ranking algorithms
- [ ] Application tracking system
- [ ] Notion integration for job management

### Planned for v0.5.0
- [ ] Analytics dashboard
- [ ] Email notifications
- [ ] Automated application submissions
- [ ] Cover letter generation
- [ ] Follow-up reminder system

---

## Development Notes

### Technical Debt
- None identified at this stage

### Known Issues
- None identified at this stage

### Dependencies
See `requirements.txt` for full dependency list and versions.

### Contributing
This is a personal project. For questions or suggestions, please open an issue.

---

*Last Updated: November 9, 2025*
