import requests

def searchAttraction(searchType, searchValues):
        resp= requests.get(f"https://api.stb.gov.sg/content/attractions/v2/search?searchType={searchType}&searchValues={searchValues}", 
                            headers= {
                                'Content-Type': 'application/json',
                                'X-API-Key': "DASlrNGgWJ8cQv7HASyowi1SFXAta77c",
                            }
                        )
        print(resp)
        return resp
        