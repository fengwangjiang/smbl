
#USE_HOME=1

# use user's home directory (to share the already compiled programs)?

FA_EXAMPLE   = "example_fasta.fa"
FA_HG39 = "hg39.fa"

try:
	USE_HOME
except NameError:
	USE_HOME=False

if USE_HOME:
	bin_dir = os.path.join(os.path.expanduser("~"),".snakemake-lib","bin")
else:
	bin_dir = "bin"

print("directory for programs: ",bin_dir)

PROG_ART_454         = os.path.join(bin_dir,"art_454")
PROG_ART_ILLUMINA    = os.path.join(bin_dir,"art_illumina")
PROG_ART_SOLID       = os.path.join(bin_dir,"art_solid")
PROG_BCFTOOLS        = os.path.join(bin_dir,"bcftools")
PROG_BGZIP           = os.path.join(bin_dir,"bgzip")
PROG_BWA             = os.path.join(bin_dir,"bwa")
PROG_DWGSIM          = os.path.join(bin_dir,"dwgsim")
PROG_SAMTOOLS        = os.path.join(bin_dir,"samtools")
PROG_TABIX           = os.path.join(bin_dir,"tabix")

ALL_PROGS = (
		PROG_DWGSIM,
		PROG_ART_454,
		PROG_ART_ILLUMINA,
		PROG_ART_SOLID,
		PROG_BCFTOOLS,
		PROG_BGZIP,
		PROG_BWA,
		PROG_SAMTOOLS,
		PROG_TABIX
	)

ALL_FAS = (
		FA_EXAMPLE
	)

ALL_FAIS = expand("{fa}.fai", fa=ALL_FAS)