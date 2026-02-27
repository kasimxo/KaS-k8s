{{- define "network-monitoring.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "network-monitoring.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "network-monitoring.labels" -}}
app.kubernetes.io/name: {{ include "network-monitoring.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
