require 'asciidoctor'
require File.dirname(__FILE__) + '/asciidoctor_patch'
require File.dirname(__FILE__) + '/requirement_block'

Asciidoctor::Extensions.register do |document|
  block :requirement, RequirementBlock
end