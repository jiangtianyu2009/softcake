from scrapinghub import ScrapinghubClient

apikey = '11befd9da9304fecb83dfa114d1926e9'
client = ScrapinghubClient(apikey)
project = client.get_project(252342)
project.jobs.run('javname')
project.jobs.run('thzride')
project.jobs.run('thzwalk')
