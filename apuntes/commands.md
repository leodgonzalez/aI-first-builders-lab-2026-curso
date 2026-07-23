# 1. Cargá el entorno de .NET (pone dotnet en el PATH)
source ~/.dotnet_env

# 2. Parate en el backend
cd /mnt/c/dev/educacion/202606-ai-first-builders-lab/src/modulo-3/backend

# 3. Corré el test
dotnet test tests/Reservas.Tests/Reservas.Tests.csproj -l "console;verbosity=detailed"
