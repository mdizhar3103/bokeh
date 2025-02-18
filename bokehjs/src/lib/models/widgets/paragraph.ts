import {Markup, MarkupView} from "./markup"
import {p as paragraph} from "core/dom"
import * as p from "core/properties"

export class ParagraphView extends MarkupView {
  override model: Paragraph

  override render(): void {
    super.render()
    // This overrides default user-agent styling and helps layout work
    const content = paragraph({style: {margin: 0}}, this.model.text)
    this.markup_el.appendChild(content)
  }
}

export namespace Paragraph {
  export type Attrs = p.AttrsOf<Props>

  export type Props = Markup.Props
}

export interface Paragraph extends Paragraph.Attrs {}

export class Paragraph extends Markup {
  override properties: Paragraph.Props
  override __view_type__: ParagraphView

  constructor(attrs?: Partial<Paragraph.Attrs>) {
    super(attrs)
  }

  static {
    this.prototype.default_view = ParagraphView
  }
}
