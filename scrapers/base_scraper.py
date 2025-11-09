"""
Base scraper class providing common functionality for all job board scrapers.
"""

from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
import time
import logging

class BaseScraper(ABC):
    """
    Abstract base class for all job board scrapers.
    
    Supports both simple HTTP requests and Selenium fallback.
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def scrape_jobs(self, keyword, location=None, limit=10):
        """
        Scrape jobs from the job board.
        
        Args:
            keyword (str): Search keyword
            location (str, optional): Location filter
            limit (int): Maximum number of results
        
        Returns:
            list: List of job dictionaries
        """
        pass
    
    def _make_request(self, url, params=None, method='GET'):
        """
        Make HTTP request with error handling and rate limiting.
        
        Args:
            url (str): URL to request
            params (dict, optional): Query parameters
            method (str): HTTP method
        
        Returns:
            requests.Response: Response object
        """
        try:
            # Apply rate limiting
            rate_limit = self.config.get('rate_limit', 1.0)
            time.sleep(rate_limit)
            
            if method == 'GET':
                response = self.session.get(url, params=params, timeout=10)
            else:
                response = self.session.post(url, data=params, timeout=10)
            
            response.raise_for_status()
            return response
        
        except requests.RequestException as e:
            self.logger.error(f"Request failed for {url}: {e}")
            raise
    
    def _parse_html(self, html):
        """
        Parse HTML content with BeautifulSoup.
        
        Args:
            html (str): HTML content
        
        Returns:
            BeautifulSoup: Parsed HTML
        """
        return BeautifulSoup(html, 'lxml')
    
    def _normalize_job(self, job_data, source):
        """
        Normalize job data to standard format.
        
        Args:
            job_data (dict): Raw job data
            source (str): Source board name
        
        Returns:
            dict: Normalized job data
        """
        return {
            'title': job_data.get('title', '').strip(),
            'company': job_data.get('company', '').strip(),
            'location': job_data.get('location', '').strip(),
            'description': job_data.get('description', '').strip(),
            'url': job_data.get('url', '').strip(),
            'salary': job_data.get('salary', '').strip(),
            'posted_date': job_data.get('posted_date', ''),
            'source': source,
        }
