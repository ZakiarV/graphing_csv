import matplotlib.pyplot as plt
import os
from src.get_data.get_data import GetData


class Graph:
    def __init__(self, flags, data):
        self.flags = flags
        self.data = data
        self.mode = self.set_mode()

    def set_mode(self):
        if self.flags["mode"] == "physics":
            self.mode = "physics"
        elif self.flags["mode"] == "static":
            self.mode = "static"
        else:
            raise ValueError("Invalid mode. Choose 'physics' or 'static'.")
        return self.mode

    def plot(self):
        if self.mode == "physics":
            self.plot_physics()
        elif self.mode == "static":
            self.plot_static()

    def get_physics_plot_naming_parameters(self):
        if "experiment" in self.flags:
            experiment = self.flags["experiment"]
        elif "e" in self.flags:
            experiment = self.flags["e"]
        else:
            raise ValueError("No experiment name or number provided. Use --experiment to specify the experiment name or number.")
        if "object" in self.flags:
            object = self.flags["object"]
        elif "o" in self.flags:
            object = self.flags["o"]
        else:
            raise ValueError("No object name provided. Use --object to specify the object name. If no object was used, use --object=none.")
        if "question" in self.flags:
            question = self.flags["question"]
        elif "q" in self.flags:
            question = self.flags["q"]
        else:
            raise ValueError("No question number provided. Use --question to specify the question number. If no question was asked, use --question=none.")
        if "output_folder" in self.flags:
            output_folder = self.flags["output_folder"]
        elif "o" in self.flags:
            output_folder = self.flags["o"]
        else:
            output_folder = experiment
        if "single_plot" in self.flags:
            single_plot = self.flags["single_plot"]
        elif "s" in self.flags:
            single_plot = self.flags["s"]
        else:
            single_plot = False
        if "get_data" in self.flags:
            get_data = self.flags["get_data"]
        elif "g" in self.flags:
            get_data = self.flags["g"]
        else:
            get_data = False
        return experiment, object, question, output_folder, single_plot, get_data

    def plot_physics(self):
        experiment, object_, question, output_folder, single_plot, get_data = self.get_physics_plot_naming_parameters()
        folder_name = f"{output_folder}"
        experiment_folder = f"{folder_name}/{experiment}"
        question_folder = f"{experiment_folder}/{question}"
        assert self.data["time"] is not None, "Time data is required for physics mode."
        if not os.path.exists(question_folder):
            os.makedirs(question_folder)
        if self.data["position"] is not None:
            plt.plot(self.data["time"], self.data["position"])
            plt.ylabel("Position (m)")
            plt.xlabel("Time (s)")
            if not single_plot:
                if object_ == "none":
                    plt.title(f"{question}: Position vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_position_vs_time.png")
                else:
                    plt.title(f"{question} - {object_}: Position vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_{object_}_position_vs_time.png")
                plt.clf()
            if get_data:
                data = GetData(self.data["position"], question_folder, f"{experiment}_{question}_position_vs_time", data_type="position")
                data.write_data()
        if self.data["velocity"] is not None:
            plt.plot(self.data["time"], self.data["velocity"])
            plt.ylabel("Velocity (m/s)")
            plt.xlabel("Time (s)")
            if not single_plot:
                if object_ == "none":
                    plt.title(f"{question}: Velocity vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_velocity_vs_time.png")
                else:
                    plt.title(f"{question} - {object_}: Velocity vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_{object_}_velocity_vs_time.png")
                plt.clf()
            if get_data:
                data = GetData(self.data["velocity"], question_folder, f"{experiment}_{question}_velocity_vs_time", data_type="velocity")
                data.write_data()
        if self.data["acceleration"] is not None:
            plt.plot(self.data["time"], self.data["acceleration"])
            plt.ylabel("Acceleration (m/s²)")
            plt.xlabel("Time (s)")
            if not single_plot:
                if object_ == "none":
                    plt.title(f"{question}: Acceleration vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_acceleration_vs_time.png")
                else:
                    plt.title(f"{question} - {object_}: Acceleration vs Time")
                    plt.savefig(f"{question_folder}/{experiment}_{question}_{object_}_acceleration_vs_time.png")
                plt.clf()
            if get_data:
                data = GetData(self.data["acceleration"], question_folder, f"{experiment}_{question}_acceleration_vs_time", data_type="acceleration")
                data.write_data()
        if single_plot:
            plt.legend(["Position", "Velocity", "Acceleration"])
            if object_ == "none":
                plt.title(f"{question}: Position, Velocity, and Acceleration vs Time")
                plt.savefig(f"{question_folder}/{experiment}_{question}_position_velocity_acceleration_vs_time.png")
            else:
                plt.title(f"{question} - {object_}: Position, Velocity, and Acceleration vs Time")
                plt.savefig(f"{question_folder}/{experiment}_{question}_{object_}_position_velocity_acceleration_vs_time.png")
            plt.clf()

    def plot_static(self):
        pass