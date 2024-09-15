# file_manager_node.py

import os
from typing import Tuple
from nodes import NODE_CLASS_MAPPINGS, CommonNode

class FileManagerNode(CommonNode):
    """
    A ComfyUI custom node that lists files in a directory and reads file contents.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {
                    "default": ".",
                    "multiline": False,
                    "placeholder": "Enter directory path"
                }),
                "filename": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "placeholder": "Enter filename to read (optional)"
                }),
            }
        }

    RETURN_TYPES = ("STRING", "BYTES")
    RETURN_NAMES = ("file_list", "file_content")
    FUNCTION = "manage_files"
    CATEGORY = "Utilities/File Management"
    OUTPUT_IS_LIST = (False, False)

    def manage_files(self, path: str, filename: str) -> Tuple[str, bytes]:
        try:
            # List all files, including hidden files
            file_list = os.listdir(path)
            file_list_str = "\n".join(file_list)

            file_content = b""
            if filename:
                full_path = os.path.join(path, filename)
                if os.path.isfile(full_path):
                    with open(full_path, 'rb') as f:
                        file_content = f.read()
                else:
                    file_content = b"File not found."
            return (file_list_str, file_content)
        except Exception as e:
            error_message = f"Error: {e}"
            return (error_message, b"")

# Register the node
NODE_CLASS_MAPPINGS.update({
    "FileManagerNode": FileManagerNode
})
