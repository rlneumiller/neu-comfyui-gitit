import json
import os

import folder_paths


class ComfyUIGitIt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "filename_prefix": ("STRING", {"default": "ComfyUI-GitIt/workflow"}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "export_workflows"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def export_workflows(self, filename_prefix="ComfyUI-GitIt/workflow", prompt=None, extra_pnginfo=None):
        output_dir = folder_paths.get_output_directory()
        full_output_folder, filename, counter, _, _ = folder_paths.get_save_image_path(
            filename_prefix, output_dir
        )
        os.makedirs(full_output_folder, exist_ok=True)

        base_path = os.path.join(full_output_folder, f"{filename}_{counter:05d}")
        gui_workflow = extra_pnginfo.get("workflow") if extra_pnginfo else None
        if gui_workflow is None:
            raise ValueError("The GUI workflow was not supplied by ComfyUI")
        if prompt is None:
            raise ValueError("The API workflow was not supplied by ComfyUI")

        gui_path = f"{base_path}_gui.json"
        api_path = f"{base_path}_api.json"
        with open(gui_path, "w", encoding="utf-8") as file:
            json.dump(gui_workflow, file, ensure_ascii=False, indent=2)
            file.write("\n")
        with open(api_path, "w", encoding="utf-8") as file:
            json.dump(prompt, file, ensure_ascii=False, indent=2)
            file.write("\n")

        return {"ui": {"text": [f"Exported {gui_path} and {api_path}"]}}


NODE_CLASS_MAPPINGS = {
    "ComfyUIGitIt": ComfyUIGitIt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUIGitIt": "ComfyUI-GitIt",
}
