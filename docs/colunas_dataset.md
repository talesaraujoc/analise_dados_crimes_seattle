## 📌 Tabela de Colunas do Dataset de Crimes (Seattle Police Department)

| **Nome da Coluna**                  | **Descrição** |
|--------------------------------------|--------------|
| **Número do Relatório** (`report_number`) | Identificador único do relatório geral. Um relatório pode conter múltiplas infrações, indicadas pelo ID da infração. |
| **Data e Hora do Relatório** (`report_date_time`) | Data e hora em que a infração foi reportada (pode ser diferente da data de ocorrência). |
| **ID da Infração** (`offense_id`) | Identificador distinto para quando há múltiplas infrações associadas a um único relatório. |
| **Data da Infração** (`offense_date`) | Data em que a infração ocorreu. Se não estiver disponível, usa-se a data de início do evento. |
| **Grupo NIBRS AB** (`nibrs_group_a_b`) | Grupo correspondente da infração de acordo com o sistema NIBRS (National Incident-Based Reporting System). |
| **Categoria de Crime NIBRS** (`nibrs_crime_against_category`) | Categoria do crime conforme o NIBRS, indicando se é contra pessoas, propriedades ou sociedade. |
| **Subcategoria da Infração** (`offense_sub_category`) | Classificação detalhada das infrações com base nos códigos NIBRS. (Equivalente a "Infração" na versão anterior do dataset). |
| **Tipo de Tiroteio** (`shooting_type_group`) | Estatística de eventos onde houve disparos de arma de fogo. Apenas registros de "disparos" são incluídos. |
| **Endereço (Bloco)** (`block_address`) | Endereço do local da infração, mascarado para o bloco (exemplo: "100 Block Main St"). |
| **Latitude** (`latitude`) | Coordenada geográfica aproximada do local da infração (mascarada para o bloco). |
| **Longitude** (`longitude`) | Coordenada geográfica aproximada do local da infração (mascarada para o bloco). |
| **Área de Patrulha (Beat)** (`beat`) | Setor de patrulhamento onde ocorreu a infração (menor unidade de patrulha da polícia). |
| **Distrito Policial (Precinct)** (`precinct`) | Distrito policial responsável pela área onde ocorreu a infração. |
| **Setor Policial** (`sector`) | Setor maior que o "Beat", dentro do distrito policial. |
| **Bairro** (`neighborhood`) | Área designada conforme o Plano de Micro-Comunidades Policiais (MCPP). |
| **Área de Relatório** (`reporting_area`) | Área geográfica de referência usada no sistema Mark43 para localização de relatórios. |
| **Categoria da Infração** (`offense_category`) | Agrupamento das subcategorias de infrações para fins de análise (exemplo: "Crime Violento", "Crime contra Propriedade"). |
| **Descrição do Código NIBRS** (`nibrs_offense_code_description`) | Descrição oficial da infração conforme a codificação NIBRS. |
| **Código da Infração NIBRS** (`nibrs_offense_code`) | Código numérico da infração conforme o NIBRS. |

