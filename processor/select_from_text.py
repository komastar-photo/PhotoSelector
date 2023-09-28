import os
import shutil


class SelectFromText:
    @staticmethod
    def select(select_file_path, candidate_path):
        select_number_list = []
        with open(select_file_path) as select_file:
            for select_number in select_file:
                select_number_list.append(select_number.rstrip('\n'))
            print(select_number_list)

        candidate_list = os.listdir(candidate_path)
        select_list = []
        for item in candidate_list:
            for select_item in select_number_list:
                if select_item in item:
                    select_list.append(item)
                    break

        os.makedirs(os.path.join(candidate_path, 'selected'))
        for selected_filename in select_list:
            source = os.path.join(candidate_path, selected_filename)
            dest = os.path.join(candidate_path, 'selected', selected_filename)
            shutil.move(source, dest)
            print(f'move {selected_filename}')
