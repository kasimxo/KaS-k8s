{{- define "simulator.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "simulator.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "simulator.labels" -}}
app.kubernetes.io/name: {{ include "simulator.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
