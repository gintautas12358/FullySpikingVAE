#!/bin/bash
#SBATCH --gres=gpu:1

echo NetworkConfigs/events$1.yaml
echo
cat NetworkConfigs/events$1.yaml

sudo singularity exec  singularity/fsvae.sif python3 main_fsvae.py run$1 -config NetworkConfigs/events$1.yaml

