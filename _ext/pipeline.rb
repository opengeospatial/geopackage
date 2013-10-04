#
# pipeline.rb gets required automatically by Awestruct.
# I'm misusing this to require an Asciidoctor monkey patch
#

require 'asciidoctor_patch'
require 'requirement_block'

Awestruct::Extensions::Pipeline.new