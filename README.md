# ComfyUI-GitIt

From within the ComfyUI web UI - Exports both the GUI and API workflows during generation into numbered JSON files in ComfyUI's output folder in the subfolder ComfyUI-GitIt-exported.

## Install

Add this repository to `ComfyUI/custom_nodes/ComfyUI-GitIt`, restart ComfyUI, and add the `ComfyUI-GitIt` output node to a workflow.
The node uses no connections - it just works when the node is in the workflow.

## Customize workflow filename

The `filename_prefix` input supports the same output path and time variables as the installed ComfyUI version.
