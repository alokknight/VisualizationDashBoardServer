import json
from dashapi.models import DataPoint

def import_json_data():
    # Specify the path to your JSON file
    json_file_path = "C:/Users/alokknight/blackcoffer/VisualizationDashBoardServer/jsondata.json"

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        DataPoint_instance = DataPoint(
            end_year=   item['end_year'],
            intensity=  item['intensity'],
            sector=     item['sector'],
            topic=      item['topic'],
            insight=    item['insight'],
            url=        item['url'],
            region=     item['region'],
            start_year= item['start_year'],
            impact=     item['impact'],
            added=      item['added'],
            published=  item['published'],
            country=    item['country'],
            relevance=  item['relevance'],
            pestle=     item['pestle'],
            source=     item['source'],
            title=      item['title'],
            likelihood= item['likelihood'],
        )
        DataPoint_instance.save()

if __name__ == '__main__':
    import_json_data()
