import { useMemo } from "react";
import ReactQuill, {Quill} from "react-quill";
import 'react-quill/dist/quill.snow.css';
import { CustomToolbar } from './toolbar-config';
import { ImageActions } from '@xeger/quill-image-actions';
import { ImageFormats } from '@xeger/quill-image-formats';

Quill.register('modules/imageActions', ImageActions);
Quill.register('modules/imageFormats', ImageFormats);

const ReactEditor = () => {

    const formats = [
        "header", "size", "font",
        "bold", "italic", "underline", "strike", "blockquote",
        "list", "bullet", "indent", "link", "image",
        "color", "background", "align, 'float','height','width'",
        "script", "code-block", "clean",
    ];

    const modules = useMemo(() => ({
        imageActions: {},
        imageFormats: {},
        toolbar: {
            container: "#toolBar"
        },


    }), []);

    return (
        <div>
            <div id="toolBar">
                <CustomToolbar />
            </div>
            <ReactQuill theme="snow" modules={modules} formats={formats} 
                        style={{height: "300px", width: "max-w-640"}}/>
        </div>
    )
}

export default ReactEditor;