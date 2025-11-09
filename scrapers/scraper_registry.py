"""
Registry for managing job board scrapers.
"""

import logging

logger = logging.getLogger(__name__)

class ScraperRegistry:
    """
    Central registry for all job board scrapers.
    Allows dynamic registration and retrieval of scrapers.
    """
    _scrapers = {}
    
    @classmethod
    def register(cls, name, scraper_class, complexity='simple'):
        """
        Register a new scraper.
        
        Args:
            name (str): Unique identifier for the scraper
            scraper_class (class): Scraper class (must inherit from BaseScraper)
            complexity (str): 'simple' for HTTP, 'complex' for Selenium
        """
        cls._scrapers[name] = {
            'class': scraper_class,
            'complexity': complexity
        }
        logger.info(f"Registered scraper: {name} (complexity: {complexity})")
    
    @classmethod
    def get_scraper(cls, name, config=None):
        """
        Get an instance of a registered scraper.
        
        Args:
            name (str): Scraper identifier
            config (dict, optional): Configuration for the scraper
        
        Returns:
            BaseScraper: Scraper instance
        """
        if name not in cls._scrapers:
            raise ValueError(f"Scraper '{name}' not found. Available: {cls.list_all()}")
        
        scraper_class = cls._scrapers[name]['class']
        return scraper_class(config=config)
    
    @classmethod
    def list_simple_scrapers(cls):
        """Get list of HTTP-based scrapers (no Selenium required)."""
        return [name for name, info in cls._scrapers.items()
                if info['complexity'] == 'simple']
    
    @classmethod
    def list_complex_scrapers(cls):
        """Get list of Selenium-based scrapers."""
        return [name for name, info in cls._scrapers.items()
                if info['complexity'] == 'complex']
    
    @classmethod
    def list_all(cls):
        """Get list of all registered scrapers."""
        return list(cls._scrapers.keys())
    
    @classmethod
    def get_info(cls, name):
        """Get information about a specific scraper."""
        if name not in cls._scrapers:
            return None
        return cls._scrapers[name]
