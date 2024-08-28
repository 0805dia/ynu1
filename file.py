import csv


def save_to_csv(jobs):
    with open("./to_save.csv","w",newline="") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(
            ["No","공고제목","회사이름","회사위치","링크"]
        )
                            
        for index, job in enumerate(jobs):
            csv_writer.writerow(
                [index + 1,
                 job["title"],
                 job["company"],
                 job["location"],
                 job["link"]
                 ])
            