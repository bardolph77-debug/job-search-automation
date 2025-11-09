"""
Scraper for Duunitori.fi - Finland's largest job board.
"""

from scrapers.base_scraper import BaseScraper
from scrapers.scraper_registry import ScraperRegistry

class DuunitoriScraper(BaseScraper):
    """
    Scraper for Duunitori.fi
    
    Verified working - No bot protection, simple HTTP requests.
    """
    BASE_URL = "https://duunitori.fi/tyopaikat"
    
    def scrape_jobs(self, keyword, location=None, limit=10):
        """
        Scrape jobs from Duunitori.
        
        Args:
            keyword (str): Search keyword (e.g., "cybersecurity")
            location (str, optional): Location filter
            limit (int): Maximum results to return
        
        Returns:
            list: List of job dictionaries
        """
        params = {'haku': keyword}
        if location:
            params['haku'] += f" {location}"
        
        try:
            response = self._make_request(self.BASE_URL, params=params)
            soup = self._parse_html(response.text)
            
            jobs = []
            job_cards = soup.find_all('article', limit=limit)
            
            for card in job_cards:
                try:
                    job = self._extract_job_data(card)
                    if job:
                        jobs.append(self._normalize_job(job, 'Duunitori'))
                except Exception as e:
                    self.logger.warning(f"Failed to parse job card: {e}")
                    continue
            
            self.logger.info(f"Scraped {len(jobs)} jobs from Duunitori for '{keyword}'")
            return jobs
        
        except Exception as e:
            self.logger.error(f"Duunitori scraping failed: {e}")
            return []
    
    def _extract_job_data(self, card):
        """Extract job data from a job card element."""
        title_elem = card.find('h3')
        company_elem = card.find('a', href=lambda x: x and '/yritykset/' in x)
        location_elem = card.find('span', class_='location') or card.find(string=lambda x: x and '–' in str(x))
        link_elem = card.find('a', href=lambda x: x and '/tyopaikat/tyo/' in x)
        
        if not title_elem:
            return None
        
        # Extract location from text (format: "Helsinki – Published 6.11.")
        location = ''
        if location_elem:
            location_text = location_elem.get_text(strip=True) if hasattr(location_elem, 'get_text') else str(location_elem)
            if '–' in location_text:
                location = location_text.split('–')[0].strip()
        
        return {
            'title': title_elem.get_text(strip=True),
            'company': company_elem.get_text(strip=True) if company_elem else 'N/A',
            'location': location,
            'url': f"https://duunitori.fi{link_elem['href']}" if link_elem else '',
            'description': '',
            'salary': '',
            'posted_date': ''
        }

# Register the scraper
ScraperRegistry.register('duunitori', DuunitoriScraper, complexity='simple')
