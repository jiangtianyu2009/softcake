from scrapinghub import ScrapinghubClient

API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'

client = ScrapinghubClient(API_KEY)
project = client.get_project(PROJECT_ID)

# project.jobs.run('javname')
# project.jobs.run('javcode')
# project.jobs.run('javdetail')
