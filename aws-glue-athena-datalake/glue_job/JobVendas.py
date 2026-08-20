import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node ItensVendas
ItensVendas_node1787236907200 = glueContext.create_dynamic_frame.from_catalog(database="sales", table_name="itensvenda_csv", transformation_ctx="ItensVendas_node1787236907200")

# Script generated for node Clientes
Clientes_node1787238095625 = glueContext.create_dynamic_frame.from_catalog(database="sales", table_name="clientes_csv", transformation_ctx="Clientes_node1787238095625")

# Script generated for node Vendas
Vendas_node1787236374296 = glueContext.create_dynamic_frame.from_catalog(database="sales", table_name="vendas_csv", transformation_ctx="Vendas_node1787236374296")

# Script generated for node Produtos
Produtos_node1787238328131 = glueContext.create_dynamic_frame.from_catalog(database="sales", table_name="produtos_csv", transformation_ctx="Produtos_node1787238328131")

# Script generated for node Vendedores
Vendedores_node1787238362075 = glueContext.create_dynamic_frame.from_catalog(database="sales", table_name="vendedores_csv", transformation_ctx="Vendedores_node1787238362075")

# Script generated for node ItensVendasMapping
ItensVendasMapping_node1787236962322 = ApplyMapping.apply(frame=ItensVendas_node1787236907200, mappings=[("idproduto", "long", "idproduto_itensvendas", "long"), ("idvenda", "long", "idvenda_itensvendas", "long"), ("quantidade", "long", "quantidade", "long"), ("valorunitario", "double", "valorunitario", "double"), ("valortotal", "double", "valortotal", "double"), ("desconto", "double", "desconto", "double")], transformation_ctx="ItensVendasMapping_node1787236962322")

# Script generated for node VendasMapping
VendasMapping_node1787236710028 = ApplyMapping.apply(frame=Vendas_node1787236374296, mappings=[("idvenda", "long", "idvenda", "long"), ("idvendedor", "long", "idvendedor_vendas", "long"), ("idcliente", "long", "idcliente_vendas", "long"), ("data", "string", "data", "string"), ("total", "double", "total", "double")], transformation_ctx="VendasMapping_node1787236710028")

# Script generated for node JoinVendas_ItensVendas
JoinVendas_ItensVendas_node1787237877865 = Join.apply(frame1=VendasMapping_node1787236710028, frame2=ItensVendasMapping_node1787236962322, keys1=["idvenda"], keys2=["idvenda_itensvendas"], transformation_ctx="JoinVendas_ItensVendas_node1787237877865")

# Script generated for node JoinClientes
JoinClientes_node1787238168659 = Join.apply(frame1=Clientes_node1787238095625, frame2=JoinVendas_ItensVendas_node1787237877865, keys1=["idcliente"], keys2=["idcliente_vendas"], transformation_ctx="JoinClientes_node1787238168659")

# Script generated for node JoinProdutos
JoinProdutos_node1787238421977 = Join.apply(frame1=Produtos_node1787238328131, frame2=JoinClientes_node1787238168659, keys1=["idproduto"], keys2=["idproduto_itensvendas"], transformation_ctx="JoinProdutos_node1787238421977")

# Script generated for node JoinVendedores
JoinVendedores_node1787238428993 = Join.apply(frame1=Vendedores_node1787238362075, frame2=JoinProdutos_node1787238421977, keys1=["idvendedor"], keys2=["idvendedor_vendas"], transformation_ctx="JoinVendedores_node1787238428993")

# Script generated for node FinalSchemaView
FinalSchemaView_node1787239052381 = ApplyMapping.apply(frame=JoinVendedores_node1787238428993, mappings=[("desconto", "double", "desconto", "double"), ("valorunitario", "double", "valorunitario", "double"), ("valortotal", "double", "valortotal", "double"), ("sexo", "string", "sexo", "string"), ("cliente", "string", "cliente", "string"), ("total", "double", "total", "double"), ("estado", "string", "estado", "string"), ("data", "string", "data", "string"), ("quantidade", "long", "quantidade", "long"), ("nome", "string", "nome", "string"), ("status", "string", "status", "string"), ("produto", "string", "produto", "string"), ("preco", "double", "preco", "double")], transformation_ctx="FinalSchemaView_node1787239052381")

# Script generated for node DataLake
EvaluateDataQuality().process_rows(frame=FinalSchemaView_node1787239052381, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1787235131458", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
DataLake_node1787239424604 = glueContext.write_dynamic_frame.from_options(frame=FinalSchemaView_node1787239052381, connection_type="s3", format="glueparquet", connection_options={"path": "s3://aws-glue-athena-datalake-265413947475-sa-east-1-an/datalake/", "partitionKeys": ["status"]}, format_options={"compression": "snappy"}, transformation_ctx="DataLake_node1787239424604")

job.commit()