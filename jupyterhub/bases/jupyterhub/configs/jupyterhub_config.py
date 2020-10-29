from kubernetes.client import V1Capabilities, V1SELinuxOptions
spawner = c.OpenShiftSpawner
def idh_apply_pod_profile(spawner, pod):
  """Apply custom internal data hub features to pods"""

  # Apply default profile from singleuser-profiles
  apply_pod_profile(spawner, pod)

  # If GPU enabled set the selinux security context
  if spawner.gpu_mode and spawner.gpu_mode == "selinux" and \
       spawner.extra_resource_limits and "nvidia.com/gpu" in spawner.extra_resource_limits:
    # Currently a bug in RHEL Docker 1.13 whereby /dev IPC dirs get inconsistent MCS
    pod.spec.security_context.se_linux_options = V1SELinuxOptions(type='nvidia_container_t',level='s0')
  return pod

  pod.spec.hostIPC = true

spawner.modify_pod_hook = idh_apply_pod_profile
