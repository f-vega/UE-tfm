#!/usr/bin/env bash
# stop script on error
set -e

python3 simulation.py \
  --endpoint a23vjsrta09coq-ats.iot.us-east-1.amazonaws.com \
  --cert ./credentials/ac53ccfda73518c8c0ae08c5763a131137da6a62d1b8899c0bf93d4480abd4b6-certificate.pem.crt \
  --key ./credentials/ac53ccfda73518c8c0ae08c5763a131137da6a62d1b8899c0bf93d4480abd4b6-private.pem.key \
  --root-ca ./credentials/AmazonRootCA1.pem \
  --client-id Raspberrypi \
  --topic ue/thesis/dt


  # mosquitto_pub \
  # -h a23vjsrta09coq-ats.iot.us-east-1.amazonaws.com \
  # -p 8883 \
  # -t ue/thesis/dt \
  # -i "Raspberrypi" \
  # --cafile ./credentials/AmazonRootCA1.pem \
  # --cert . \
  # --key ./credentials/ac53ccfda73518c8c0ae08c5763a131137da6a62d1b8899c0bf93d4480abd4b6-private.pem.key \
  # -m '{"device": "raspberrypi", "timestamp": "2025-06-27 18:07:35", "sensores": {"weight_kg": 1.78, "temperature_c": 66.1, "vibration_ms2": 0.53}, "machine_state": "OK"}' \
  # -d
