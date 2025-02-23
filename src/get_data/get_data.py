import os


class GetData:
    def __init__(self, data, graph_folder, graph_name, data_type: str):
        self.graph_folder = graph_folder
        self.graph_name = graph_name
        self.data_type = data_type
        self.data = data
        self.remove_none()
        self.min = self.get_min()
        self.max = self.get_max()
        self.sum = self.get_sum()
        self.mean = self.get_mean()
        self.median = self.get_median()

    def remove_none(self):
        self.data = [x for x in self.data if x is not None]

    def get_min(self):
        return min(self.data)

    def get_max(self):
        return max(self.data)

    def get_sum(self):
        return sum(self.data)

    def get_mean(self):
        return self.sum / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            median = sorted_data[n//2]
        return median

    def get_data(self):
        return {
            "min": self.min,
            "max": self.max,
            "sum": self.sum,
            "mean": self.mean,
            "median": self.median
        }

    def write_data(self):
        data = self.get_data()
        if os.path.exists(f"{self.graph_folder}/{self.graph_name}_data.txt"):
            os.remove(f"{self.graph_folder}/{self.graph_name}_data.txt")
        with open(f"{self.graph_folder}/{self.graph_name}_data.txt", "w") as f:
            f.write(f"{self.graph_name}\n")
            f.write(f"{self.data_type.capitalize()}\n")
            f.write(f"Min: {data['min']}\n")
            f.write(f"Max: {data['max']}\n")
            f.write(f"Sum: {data['sum']}\n")
            f.write(f"Mean: {data['mean']}\n")
            f.write(f"Median: {data['median']}\n")
        print(f"Data written to {self.graph_folder}/{self.graph_name}_data.txt")