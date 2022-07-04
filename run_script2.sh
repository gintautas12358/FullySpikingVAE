#!/bin/bash
#SBATCH --gres=gpu:1

echo NetworkConfigs/hole$1.yaml
echo
cat NetworkConfigs/hole$1.yaml

sudo singularity exec  singularity/fsvae.sif python3 main_fsvae.py hole_run$1 -config NetworkConfigs/hole$1.yaml

