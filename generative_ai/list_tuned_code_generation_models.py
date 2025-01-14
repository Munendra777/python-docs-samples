# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_sdk_list_tuned_code_generation_models]

import vertexai
from vertexai.language_models import CodeGenerationModel


def list_tuned_code_generation_models(
    project_id: str,
    location: str,
) -> None:
    """List tuned models."""
    vertexai.init(project=project_id, location=location)
    model = CodeGenerationModel.from_pretrained("code-bison@001")
    tuned_model_names = model.list_tuned_model_names()
    print(tuned_model_names)

    return tuned_model_names


# [END aiplatform_sdk_list_tuned_code_generation_models]
if __name__ == "__main__":
    import google.auth

    PROJECT = google.auth.default()[1]
    list_tuned_code_generation_models(PROJECT, "us-central1")
