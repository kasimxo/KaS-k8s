{{- define "analytics.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "analytics.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "analytics.labels" -}}
app.kubernetes.io/name: {{ include "analytics.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
