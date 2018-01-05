from scrapinghub import ScrapinghubClient

apikey = '11befd9da9304fecb83dfa114d1926e9'
client = ScrapinghubClient(apikey)
project = client.get_project(252342)

for job in list(project.jobs.iter_last(spider='javname', state='finished')):
    javjob = job

print(javjob['key'])
job = project.jobs.get(javjob['key'])

filters = [("name", "=", ['上原結衣'])]
print(job.items.list(count=1, filter=filters))
