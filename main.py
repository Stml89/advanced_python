FILE_NAME = 'items.txt'
MAX_WEIGHT_DAG = 400


class Pack(object):
    def __init__(self, value=None, weight=None, file_name=FILE_NAME):
        self.value = value
        self.weight = weight
        self.file_name = file_name
        self.text_list = self.read_file(self.file_name)

    @staticmethod
    def read_file(file_name):
        return [line.strip().split(',') for line in open(file_name)]

    def convert_to_obj(self):
        return [type(line[0], (object,),
                     {'weight': int(line[1]), 'value': int(line[2])})
                for line in self.text_list[1:]]

    @staticmethod
    def convert_dag_to_kg(dag):
        return dag / 100

    @staticmethod
    def efficiency(item):
        return float(item.value) / float(item.weight)

    def packing(self, items, max_weight=MAX_WEIGHT_DAG):
        def pack(item):
            if item.weight <= pack.max_weight:
                pack.max_weight -= item.weight
                return True
            return False

        pack.max_weight = max_weight
        return list(filter(pack, sorted(items,
                                        key=self.efficiency,
                                        reverse=True)))


pack = Pack()
pack1 = pack.packing(pack.convert_to_obj())
total_weight = 0

for i, item in enumerate(pack1, 1):
    print("{} {} {} {}".format(i, item.__name__, item.weight, item.value))
    total_weight += item.weight

print("\nTotal weight: {0} KG".format(pack.convert_dag_to_kg(total_weight)))
