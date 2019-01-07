require 'asciidoctor'
require 'asciidoctor/extensions'
require File.dirname(__FILE__) + '/requirement_block'

Asciidoctor::Extensions.register do
  block RequirementBlock
end
