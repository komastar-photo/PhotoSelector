import os
import shutil

extension_list = ['jpg', 'jpeg', 'cr2', 'cr3', 'arw']


class SelectFromFiles:
    @staticmethod
    def select(select_path, target_path):
        selected_file_list = os.listdir(select_path)
        dst_dir_path = os.path.join(target_path, 'selected')
        if not os.path.exists(dst_dir_path):
            os.makedirs(dst_dir_path)

        for item in selected_file_list:
            filename = os.path.splitext(item)[0]
            src_full_path = os.path.join(target_path, filename)
            dst_full_path = os.path.join(dst_dir_path, filename)
            for ext in extension_list:
                src = f'{src_full_path}.{ext}'
                dst = f'{dst_full_path}.{ext}'
                if os.path.exists(src):
                    shutil.copy(src, dst)


SelectFromFiles.select('H:/PhotographyDev/test/select', 'H:/PhotographyDev/test/dst')
